import os
import time
import subprocess
import signal
import psutil
import logging


def run_abaqus_standard_sim(wrk_dir: str,
                            job: str,
                            cpus: int = 1,
                            subroutines_path: str = None,
                            restart: bool = False,
                            retry: bool = False,
                            overwrite_old: bool = False,
                            check_time: float=0.1):
    """
    Runs abaqus standard jobs on linux so that standard doesn't hang. Also handles issue when the preprocessor throws
    an error but then hangs.


    :param wrk_dir: Working directory for simulation
    :param job: Name of job (assumes this is the same name as the input file)
    :param cpus: Number of cpus for job
    :param subroutines_path: Path for subroutine file (may be relative to working directory)
    :param restart: True if this simulation is a restart of a previous simulation
    :param retry: True if there was an error the last time this simulation was submitted (can typically ignore this argument)
    :param overwrite_old: True if you would like to overwirte old job files in work directory
    :return:
    """
    start_dir = os.getcwd()
    os.chdir(wrk_dir)
    full_wrk_dir = os.getcwd()

    for ext in ['.prt', '.msg', '.sta', '.com', '.dat', '.log', '.odb', '.odb_f', '.sim']:
        file = job + ext
        if os.path.exists(file):
            if overwrite_old:
                logging.debug(f"Removing {file}")
                os.system(f'rm {file}')
            else:
                raise Exception(f'Old job files exist but overwirte_old = {overwrite_old}')

    pid = None

    command = ['abaqus',  f'job={job}', f'input={job}.inp', f'cpus={int(cpus)}']

    if subroutines_path:
        command.append(f'user={subroutines_path}')
    if restart:
        command.append(f'oldjob={restart}')

    subprocess.Popen(command)

    finished_pre = False
    failed_pre = False
    pre_error = False

    while not finished_pre:
        time.sleep(check_time)

        try:
            logging.debug("Checking if standard started")
            finished_pre = 'Run standard' in open(f"{job}.log", 'r').read()[:5000]

            if 'FATAL ERROR' in open(f"{job}.dat", 'r').read():
                finished_pre = True
                failed_pre = True
                if retry:
                    print("Pre has failed twice. Aborting...")

            if 'Abaqus Error: The executable pre' in open(f"{job}.log", 'r').read():
                finished_pre = True
                pre_error = True

            logging.debug("Not started")

        except:
            logging.debug("Couldn't check file")
            pass

    logging.info("Standard started")

    if failed_pre:
        # Kill hanging preprocessor issue (happens when preprocessor throws an error)
        for proc in psutil.process_iter():
            if proc.name() == "pre":
                logging.debug(proc)
                cmdline = proc.cmdline()
                if full_wrk_dir in cmdline:
                    pid = proc.pid
                    logging.debug("pid: ", pid)
                    break

        os.kill(pid, signal.SIGKILL)

        os.chdir(start_dir)
        raise Exception('Pre failed')

    if pre_error:
        os.chdir(start_dir)
        raise Exception('There was an error in pre')

    # time.sleep(2)

    for proc in psutil.process_iter():
        if proc.name() == "standard":
            pro_str = str(proc)
            logging.debug(pro_str)
            cmdline = proc.cmdline()
            if full_wrk_dir in cmdline:
                pid = proc.pid

    finished = False

    logging.debug(f"pid: {pid}")
    while not finished:
        time.sleep(check_time)
        try:

            finished = 'ANALYSIS SUMMARY' in open(job+".msg", 'r').read()[-5000:] or \
                       'Abaqus Error: The executable standard' in open(f"{job}.log", 'r').read()

        except:
            logging.debug("Couldn't check file")
            pass

    if pid is not None:
        if psutil.pid_exists(pid):
            for proc in psutil.process_iter():
                if proc.name() == "standard" and proc.pid == pid:
                    os.kill(pid, signal.SIGKILL)
                    logging.info("Standard completed and killed")
                    break
    else:
        os.chdir(start_dir)
        raise Exception('PID is none.')

    time.sleep(2)

    if 'Termination signal' not in open(job+".log", 'r').read():
        os.chdir(start_dir)

        raise Exception('Termination signal not in log.')

    os.chdir(start_dir)


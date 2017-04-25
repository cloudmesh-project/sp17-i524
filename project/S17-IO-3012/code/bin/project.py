#from __future__ import print_function, division
import cmd
import os
import sys
import subprocess 

class mongoCmd(cmd.Cmd):
    prompt = 'mongoCMD >>> '
    intro = 'Provided functionality to deploy a MongoDB replicated and sharded sluster.\nCommands exists to deploy, kill, benchmark, report, and view data distribution'

    #deploy
    def do_deploy(self, line):
        print('Starting deployment')
        print('Detailed deployment log files will be stored in stdlist directory.')
	commandline = "./deploy.sh " + line.strip()
	os.system(commandline)
        print('Deployment complete. Detailed log files located in stdlist directory.')

    def help_deploy(self):
        print('Run the deploy command on the command line with 5 parameters')
        print('Parameter 1: Cloud - chameleon, jetstream, or kilo (futuresystems)')
        print('Parameter 2: MongoDB Version - 34 for version 3.4, 32 for version 3.2')
        print('Parameter 3: Config Server Replication Size - a number')
        print('Parameter 4: Mongos Router Instances - a number')
        print('Parameter 5: Shard Count - a number')
        print('Parameter 6: Shard Replication Size - a number')
        print('Simple example: deploy chameleon 34 1 1 1 1')
        print('More complex example: deploy kilo 32 3 2 3 3')
        print('Note: chameleon is the most stable cloud for testing')

    #kill
    def do_kill(self, line):
        print('Deleting and undefining last cluster')
	os.system("./cluster_delete.sh")
        print('Kill complete')

    def help_kill(self):
        print('Run the kill command to delete and undefine the last cluster deployed')
        print('No Parameters')

    #benchmark
    def do_benchmark(self, line):
        print('Starting benchmark')
        commandline = "./benchmark.sh " + line.strip()
        os.system(commandline)
        print('Benchmark complete')


    def help_benchmark(self):
        print('Run the benchmark command on the command line with 1 parameter')
        print('Parameter 1: Test Size - large or small')
        print('Large used for benchmarking, but small provided for testing purposes')
        print('Example: benchmark small')
        print('Example: benchmark large')

    #report
    def do_report(self, line):
        print('Running reports')
	os.system("./report.sh")
        print('Reports complete.  All report files can be found in report directory')

    def help_report(self):
        print('Run report function to summarize all benchmarks')
        print('and generate reports in the report directory')

    #report
    def do_distribution(self, line):
        print('Data Distribution among Shards')
	subprocess.call(['./distribution.sh'])
        print('Distribution report complete')

    def help_distribution(self):
        print('Run distribution function to view the data distribution among shards')
        print('For meaningful results must be run after data is populated via benchmark test')

    def do_EOF(self, line):
        print('Exiting')
        return True



if __name__ == '__main__':
    mongoCmd().cmdloop()

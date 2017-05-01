# authors: Veera Marni 
# License: MIT
# To write hosts and slaves for ansible deployment in inventory file

import os


class HostsWriter():
    def __init__(self):

        # removing Ip config files

        # delete hosts
        if os.path.isfile("hosts") == True:
            os.remove("hosts")

        # delete sprak-defaults.conf
        if os.path.isfile("spark-defaults.conf") == True:
            os.remove("spark-defaults.conf")

        # delete spark-env.sh
        if os.path.isfile("spark-env.sh") == True:
            os.remove("spark-env.sh")

        # delete spark-env.sh
        if os.path.isfile("slaves") == True:
            os.remove("slaves")

    def writeIPs(self, staticIPs, floatingIPs, ansible_ssh_user="cc", floating_ip=False, masterIp=None):

        # hosts recreation
        file = open("hosts", "w")
        file.write("[All_nodes]\n")

        for sip, fip in zip(staticIPs, floatingIPs):
            if not floating_ip:
                fip = sip
            file.write(sip + " ansible_host=" + fip + " ansible_ssh_user="+ansible_ssh_user+ " \n")

        if masterIp != None:
            file.write(masterIp + " ansible_host=" + masterIp + " ansible_ssh_user=" + ansible_ssh_user + " \n")

        file.write("\n\n")
        file.write("[Master_node]\n")
        if masterIp == None:
            file.write(staticIPs[-1] + " ansible_host=" + floatingIPs[-1] + " ansible_ssh_user="+ansible_ssh_user+ "\n")
        else:
            file.write(masterIp + " ansible_host=" + masterIp + " ansible_ssh_user=" + ansible_ssh_user + "\n")

        file.write("\n\n")
        file.write("[Zeppelin_node]\n")
        if masterIp == None:
            file.write(staticIPs[-1] + " ansible_host=" + floatingIPs[-1] + " ansible_ssh_user="+ansible_ssh_user+ "\n")
            print 'Master node is at: ' + floatingIPs[-1]
        else:
            file.write(
                masterIp + " ansible_host=" + masterIp + " ansible_ssh_user=" + ansible_ssh_user + "\n")

        file.close()

        # sprak-defaults.conf recreation
        file = open("spark-defaults.conf", "w")
        if masterIp == None:
            file.write("spark.master    spark://" + staticIPs[-1] + ":8081")
        else:
            file.write("spark.master    spark://" + masterIp + ":8081")
        file.close()

        # spark-env.sh recreation
        file = open("spark-env.sh", "w")
        file.write("# config file to be distributed across cluster \n")
        if masterIp == None:
            file.write("SPARK_MASTER_HOST=" + staticIPs[-1] + "\n")
        else:
            file.write("SPARK_MASTER_HOST=" + masterIp + "\n")
        file.write("SPARK_MASTER_PORT=8081\n")
        file.write("SPARK_MASTER_WEBUI_PORT=8082\n")
        file.close()

        # slaves recreation
        file = open("slaves", "w")

        if masterIp==None:
            if len(staticIPs) > 1:
                for sip in staticIPs[:-1]:
                    file.write(sip + "\n")
            elif len(staticIPs) == 1:
                file.write(staticIPs[-1])
        else:
            for sip in staticIPs:
                file.write(sip + "\n")

        file.close()

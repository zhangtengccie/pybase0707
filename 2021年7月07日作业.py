#第一题
import paramiko


def ssh_cli(ip, username, password, port=22, cmd='ls'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=port, username=username, password=password, timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    return x
#


#第二题
import re
def ssh_get_route(ip,username,password,port=22):
    route_result = ssh_cli(ip,username,password,cmd='route -n')
    for route in route_result.split('\n')[2:-1]:
        re_route = re.match(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}\s+'
                            r'(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+'
                            r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}\s+'
                            r'(\w+)\s+\d+\s+\d+\s+\d+ \w+',route.strip())
        if re_route:
            if re_route.groups()[1] == 'UG':
                return re_route.groups()[0]
if __name__ == '__main__':
    # print(ssh_cli('1.1.1.128', 'root', '123456', cmd='route'))
    print('网关为：')
    print(ssh_get_route('1.1.1.128','root','123456'))

import subprocess

user = ''
password = ''
ip_start = '0.0.0'
ip_end = '0'

file = './cam_script_log'
with open(file) as content:
  last_logged_ip = content.read().strip()
  if last_logged_ip:
    ip_end = last_logged_ip

def open_cam(user, password, ip_start, num):
  command = 'ffplay'
  arg1 = '-an'
  arg2 = '-hide_banner' 
  arg3 = f'rtsp://{user}:{password}@{ip_start}.{num}:554/onvif1'
  result = subprocess.run([command, arg1, arg2, arg3], capture_output=True)
  return result

execute_function = open_cam(user, password, ip_start, ip_end)

if(str(execute_function.stderr).__contains__('failed')):
  for number in range(10,50):
    if (not str(open_cam(user, password, ip_start, number).stderr).__contains__('failed')):
      execute_function
      with open(file, 'w') as last_logged_ip:
        last_logged_ip.write(str(number))
      break

import subprocess
data = subprocess.check_output(['netsh', 'wlan','show','profiles']).decode('uft-8').split('\n')
profiles = [i.split(":")[1][1:-1]for i in data if "All User Profiles" in i]
for i in profiles:
  results = subprocess.check_output(['netsh', 'wlan','show','profiles','i','keyclear']).decode('uft-8').split('\n')
  results = [b.split(":")[1][1:-1]for b in results if "Key Content" in b]
  try:
    print("{:<30}| {:<}".format(i,result[0]))
  expect IndexError:
    print("{:<30}| {:<}".format(i,""))
    

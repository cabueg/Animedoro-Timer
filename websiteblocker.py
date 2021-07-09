from datetime import datetime


sites_to_block = ['www.facebook.com', 'facebook.com','www.instagram.com','instagram.com',
'www.youtube.com','youtube.com','www.reddit.com','reddit.com']

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"


redirect = "127.0.0.1"

def blockSites():
    print("Block sites")
    with open(hosts_path, 'r+') as hostfile:
        hosts_content = hostfile.read()
        for site in  sites_to_block:
            if site not in hosts_content:
                hostfile.write(redirect + ' ' + site + '\n')

def unblockSites():
        print('Unblock sites')
        with open(hosts_path, 'r+') as hostfile:
            lines = hostfile.readlines()
            hostfile.seek(0)
            for line in lines:
                if not any(site in line for site in sites_to_block):
                    hostfile.write(line)
            hostfile.truncate()


# sudo python main.py
if __name__ == '__main__':
    blockSites()
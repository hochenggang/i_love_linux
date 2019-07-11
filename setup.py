# coding=utf-8
import os


def main():
    if not os.path.isdir("/www"):
        os.makedirs("/www")

    os.system("cd /www")

    # 检查 caddy 是否已经被安装
    if not os.path.isfile("/usr/local/bin/caddy"):
        # 若没有，则执行安装脚本
        os.system("curl https://getcaddy.com | bash -s personal")
    
    # 再次检查
    if not os.path.isfile("/usr/local/bin/caddy"):
        # 终止
        print("failed to install caddyserver")
        return
    
    # 拉取代码
    os.system("yum -y install git")
    os.system("git clone https://github.com/hechenggang/flask_app_manager.git")
    
    venv_path = os.path.join("/www/flask_app_manager", "venv")
    os.makedirs(venv_path)
    os.system("python3.7 -m venv {}".format(venv_path))

    os.system("{} install -r {} -i https://pypi.tuna.tsinghua.edu.cn/simple/".format(
            os.path.join(app_dir, "venv", "bin", "pip3.7"), 
            os.path.join(app_dir, "requirements.txt")
        ))

if __name__ == "__main__":
    main()



# ssh -p 9527 -l root t.imhcg.cn
# cd /www/flask_app_manager
# venv/bin/python3.7 app.py
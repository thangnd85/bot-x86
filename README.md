# lbminh-bot-test
Test build for tester and developer.

Contribute develope team to improve product.

Momo / ViettelPay: 0985 435 685 

----------------------------------------
Phiên bản dành cho tester và nhà phát triển:

Hãy ủng hộ team để cùng phát triển sản phẩm hoàn thiện. 

Momo / ViettelPay: 0985 435 685 
-----------------------------------------
How to install - Hướng dẫn cài đặt

Login with user 'pi' then use following command to install

Đăng nhập với user 'pi' và dùng các lệnh sau để cài đặt
    
    git clone https://github.com/thangnd85/lbminh-bot-test/

    cd /home/pi/lbminh-bot-test
    
    python3 setupLBMINHBOT.py

Manual start - Cách thủ công (dể debug lỗi)

* Normal env - Môi trường thông thường (số 1 trong cài đặt)
  
      cd /home/pi/lbminh-bot-test
  
      python3 main.py

*Virtual env - Môi trường ảo (số 2 trong cài đặt)
  
     cd /home/pi/lbminh-bot-test
  
    ./bot.sh

Automatically start - Khởi động tự động:
  
    sudo systemctl start bot.service

Remember that you have to use Spotify Premium for this build. 

And you have to authenticate with Spotify at first start.

Ghi nhớ: Bạn phải có tài khoản Spotify Premium và cấu hình nó trong config.yaml


HOW TO UPDATE:

    cd lbminh-bot-test
    git pull
    python3 setupLBMINHBOT.py 

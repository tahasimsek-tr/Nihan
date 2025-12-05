Nihan – Pre‑Attack Cloaking Tool

Overview
Nihan is a lightweight CLI utility for Kali Linux that prepares a system for a penetration test by hiding its network footprint (IP, MAC, DNS) and cleaning logs before any active attack is launched.

Installation / Kurulum

# Required packages (run once)
sudo apt update
sudo apt install -y tor proxychains macchanger openssh-client dnscrypt-proxy srm

# Download Nihan
wget -O nihan.py 
chmod +x nihan.py


Usage / Kullanım

sudo ./nihan.py


Warning / Uyarı

En

This software is intended only for authorized security testing. By using Nihan you agree to the following:

Authorized Environments Only – Run the tool only on machines, networks, or services you own, manage, or have explicit permission to test.
Legal Responsibility – Unauthorized access, data theft, denial‑of‑service, or any other illegal activity is strictly prohibited and may result in criminal prosecution.
Security Risks – Features such as Tor, SSH tunneling, and MAC spoofing can disrupt network behavior if mis‑configured. Test thoroughly and back up critical data before use.
Forensic Impact – Log wiping and DNS encryption erase evidence that could be required for incident response or legal investigations.
No Warranty / Liability – Nihan is provided as‑is, free of charge, with no warranties or support. The authors are not liable for any damage, loss, or legal consequences arising from its use.
By running the program you acknowledge that you have read, understood, and will comply with the above conditions.

Tr

Bu yazılım yalnızca yetkili güvenlik testleri için tasarlanmıştır. Nihan’ı kullanarak aşağıdakileri kabul etmiş sayılırsınız:

Yalnızca Yetkili Ortamlar – Aracı sadece sahip olduğunuz, yönettiğiniz veya açıkça izin verilen sistem, ağ veya hizmetlerde çalıştırın.
Yasal Sorumluluk – İzinsiz erişim, veri hırsızlığı, hizmeti aksatma (DoS) ve benzeri yasa dışı faaliyetler kesinlikle yasaktır ve cezai yaptırımlara tabi olabilir.
Güvenlik Riski – Tor, SSH tüneli ve MAC spoofing gibi özellikler yanlış yapılandırıldığında ağda beklenmeyen davranışlara yol açabilir. Kullanımdan önce kapsamlı test yapın ve kritik verilerin yedeğini alın.
Adli İzleme Etkisi – Log silme ve DNS şifreleme, olay incelemesi veya yasal soruşturma için gerekli kanıtların kaybolmasına neden olabilir.
Garanti ve Sorumluluk Reddi – Nihan ücretsiz, açık kaynak ve herhangi bir garanti, destek veya sorumluluk olmaksızın sunulmaktadır. Geliştiriciler, kullanım sonucu ortaya çıkan zarar, kayıp veya yasal sonuçlardan sorumlu değildir.
Programı çalıştırarak bu koşulları okuduğunuzu, anladığınızı ve bunlara uyacağınızı kabul etmiş olursunuz.

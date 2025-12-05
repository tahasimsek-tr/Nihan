#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Nihan – Saldırı öncesi gizlenme aracı
Kali Linux için hazırlanmıştır.
"""

import subprocess
import sys
import time
import random
from pathlib import Path

# -------------------------------------------------
# Yardımcı fonksiyonlar
# -------------------------------------------------
def run_cmd(cmd, capture=False):
    """Komutu çalıştır, hata olursa çık."""
    try:
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE if capture else None,
            stderr=subprocess.STDOUT,
            check=True,
            text=True,
        )
        if capture:
            return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"[!] Hata: {' '.join(cmd)}")
        print(e.stdout)
        sys.exit(1)

def sudo_cmd(cmd):
    return ["sudo"] + cmd

def random_delay():
    d = random.randint(5, 15)
    print(f"[i] {d}s bekleniyor...")
    time.sleep(d)

# -------------------------------------------------
# Gizlenme adımları
# -------------------------------------------------
def mac_spoof(iface="wlan0"):
    print("[i] MAC adresi değiştiriliyor...")
    run_cmd(sudo_cmd(["macchanger", "-r", iface]))
    random_delay()

def start_tor():
    print("[i] Tor servisi başlatılıyor...")
    run_cmd(sudo_cmd(["systemctl", "restart", "tor"]))
    random_delay()

def proxychains_scan(target):
    print("[i] proxychains üzerinden nmap çalıştırılıyor...")
    run_cmd(["proxychains", "nmap", "-sT", "-Pn", target])

def start_dnscrypt():
    print("[i] dnscrypt-proxy servisi yeniden başlatılıyor...")
    run_cmd(sudo_cmd(["systemctl", "restart", "dnscrypt-proxy"]))
    random_delay()

def ssh_tunnel(host):
    print("[i] SSH SOCKS5 tüneli (localhost:1080) kuruluyor...")
    proc = subprocess.Popen(
        ["ssh", "-N", "-D", "1080", host],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    # 30 s örnek bekleme; gerçek senaryoda daha uzun tutabilirsiniz
    time.sleep(30)
    proc.terminate()
    print("[i] SSH tüneli kapatıldı.")

def clean_logs():
    print("[i] /var/log dizini güvenli şekilde siliniyor...")
    # srm (secure-delete) paketinin kurulu olduğunu varsayıyoruz
    run_cmd(sudo_cmd(["srm", "-r", "-z", "-m", "/var/log"]))
    random_delay()

# -------------------------------------------------
# Senaryolar
# -------------------------------------------------
def scenario_basic():
    """IP anonimleştirme + MAC spoof + basit tarama"""
    mac_spoof()
    start_tor()
    target = input("Tarama hedefi (IP/alan): ").strip()
    proxychains_scan(target)

def scenario_full():
    """Tam gizlenme: MAC, Tor, DNS‑crypt, SSH tünel, log temizleme"""
    mac_spoof()
    start_tor()
    start_dnscrypt()
    ssh_host = input("SSH tünel hedefi (user@host): ").strip()
    ssh_tunnel(ssh_host)
    clean_logs()

def main():
    print("\n=== Nihan – Saldırı Öncesi Gizlenme ===")
    print("1 – Temel anonim tarama (MAC + Tor + proxychains)")
    print("2 – Tam gizlenme (MAC + Tor + DNScrypt + SSH tünel + log temizleme)")
    choice = input("Seçiminiz (1/2): ").strip()

    if choice == "1":
        scenario_basic()
    elif choice == "2":
        scenario_full()
    else:
        print("[!] Geçersiz seçim.")
        sys.exit(1)

    print("\n[✓] Gizlenme adımları tamamlandı.")

if __name__ == "__main__":
    # root ayrıcalıkları gereklidir
    if not Path("/usr/bin/sudo").exists():
        print("[!] sudo bulunamadı – script root ayrıcalıklarıyla çalıştırılmalı.")
        sys.exit(1)
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ==============================================================
#   N I H A N  –  Pre‑Attack Cloaking Tool
# ==============================================================

def nihan_logo(baslik_renk="cyan", alt_yazi=True):
    
    renkler = {
        "cyan":   "\033[96m",
        "pink":   "\033[95m",
        "purple": "\033[95m",
        "blue":   "\033[94m",
        "yellow": "\033[93m",
        "green":  "\033[92m",
        "red":    "\033[91m",
        "white":  "\033[97m",
    }
    renk = renkler.get(baslik_renk.lower(), "\033[96m")
    reset = "\033[0m"

    logo = f"""
{renk}    ███╗   ██╗██╗██╗  ██╗ █████╗ ███╗   ██╗
    ████╗  ██║██║██║  ██║██╔══██╗████╗  ██║
    ██╔██╗ ██║██║███████║███████║██╔██╗ ██║
    ██║╚██╗██║██║██╔══██║██╔══██║██║╚██╗██║
    ██║ ╚████║██║██║  ██║██║  ██║██║ ╚████║
    ╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝{reset}
"""
    print(logo)
    if alt_yazi:
        print(f"{' ' * 18}{renk}♡ Made with love in Python ♡{reset}")
    print()   


import subprocess
import sys
import time
import random
from pathlib import Path

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
    time.sleep(30)         
    proc.terminate()
    print("[i] SSH tüneli kapatıldı.")

def clean_logs():
    print("[i] /var/log dizini güvenli şekilde siliniyor...")
    run_cmd(sudo_cmd(["srm", "-r", "-z", "-m", "/var/log"]))
    random_delay()


def scenario_basic():
    """IP anonimleştirme + MAC spoof + basit tarama"""
    mac_spoof()
    start_tor()
    target = input("Tarama hedefi (IP/alan): ").strip()
    proxychains_scan(target)

def scenario_full():
    """Tam gizlenme: MAC + Tor + DNScrypt + SSH tünel + log temizleme"""
    mac_spoof()
    start_tor()
    start_dnscrypt()
    ssh_host = input("SSH tünel hedefi (user@host): ").strip()
    ssh_tunnel(ssh_host)
    clean_logs()

def main():
    
    nihan_logo("pink")          

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
   
    if not Path("/usr/bin/sudo").exists():
        print("[!] sudo bulunamadı – script root ayrıcalıklarıyla çalıştırılmalı.")
        sys.exit(1)
    main()

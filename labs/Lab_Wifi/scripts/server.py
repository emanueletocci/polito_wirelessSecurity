import subprocess

def main():
    print("=== iperf Server Mode ===")
    protocol = input("Protocol (tcp/udp): ").strip().lower()
    
    cmd = ["iperf", "-s"]
    if protocol == "udp":
        cmd.append("-u")
        
    print(f"\nGenerated iperf command: {' '.join(cmd)}")
    print("Server listening... Press Ctrl+C to stop.\n")
    
    try:
        subprocess.run(cmd)
    except KeyboardInterrupt:
        print("\nServer execution interrupted by user.")
    except FileNotFoundError:
        print("\nError: iperf is not installed or not in the system PATH.")

if __name__ == "__main__":
    main()
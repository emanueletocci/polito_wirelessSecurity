import subprocess

def main():
    print("=== iperf Server Mode ===")
    protocol = input("Do you want to use TCP or UDP? (type tcp or udp): ").strip().lower()
    
    cmd = ["iperf", "-s"]
    if protocol == "udp":
        cmd.append("-u")
        print("Starting the server in UDP mode...")
    else:
        print("Starting the server in TCP mode...")
        
    print(f"Executing command: {' '.join(cmd)}")
    print("Press Ctrl+C to stop the server.\n")
    
    try:
        # Executes iperf in server mode and leaves it listening
        subprocess.run(cmd)
    except KeyboardInterrupt:
        print("\nServer execution interrupted by user.")
    except FileNotFoundError:
        print("\nError: iperf is not installed or not in the system PATH.")

if __name__ == "__main__":
    main()
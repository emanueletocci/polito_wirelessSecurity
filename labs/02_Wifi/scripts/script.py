import subprocess
import re
import statistics
import time
import sys

def run_server():
    print("\n--- Server Mode ---")
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

def run_client():
    print("\n--- Client Mode ---")
    server_ip = input("Enter the server IP address: ").strip()
    protocol = input("Do you want to use TCP or UDP? (type tcp or udp): ").strip().lower()
    method = input("Do you want to use standard or reverse mode? (type standard or reverse): ").strip().lower()
    
    cmd_base = ["iperf", "-c", server_ip, "-i", "1"]
    
    if protocol == "udp":
        cmd_base.append("-u")
        print("You chose UDP. The -u flag will be added.")
    else:
        print("You chose TCP.")
        
    if method == "reverse":
        cmd_base.append("-R")
        print("You chose reverse mode. The -R flag will be added.")
    else:
        print("You chose standard mode.")
        
    log_file = f"log_{protocol}_{server_ip}.txt"
    print(f"\nStarting the tests. The results will be saved and appended in: {log_file}")
    print("---------------------------------------------------")
    
    throughputs = []
    
    for i in range(1, 11):
        print(f"Running: Test {i} of 10...")
        
        # Writing the EXACT header into the log file requested by the user
        with open(log_file, "a") as f:
            f.write(f"--- Test {i} of 10 ---\n")
            
        try:
            # Executing the iperf command capturing the textual output
            result = subprocess.run(cmd_base, capture_output=True, text=True, check=True)
            output = result.stdout
            
            # Saving the entire original-style output into the log file
            with open(log_file, "a") as f:
                f.write(output)
                
            # Extracting the throughput for statistical calculations.
            # It also intercepts milliseconds (e.g., "0.0000-10.0156 sec")
            match = re.search(r"0\.0+-10\.\d+\s+sec.*?\s+(\d+(?:\.\d+)?)\s+[M|G]bits/sec", output)
            
            if match:
                val = float(match.group(1))
                throughputs.append(val)
                print(f" -> Completed: recorded a throughput of {val} Mbits/sec")
            else:
                print(" -> Warning: Test finished, but unable to extract summary data for statistics.")
                
        except subprocess.CalledProcessError as e:
            print(f"Error during iperf execution in test {i}.")
            print(e.stderr)
        except FileNotFoundError:
            print("\nError: iperf is not installed on this system.")
            sys.exit(1)
            
        time.sleep(1)

    print("---------------------------------------------------")
    print("All 10 measurements have been successfully completed!")
    print("\n--- STATISTICAL RESULTS (Mbits/sec) ---")
    
    if throughputs:
        avg = statistics.mean(throughputs)
        min_val = min(throughputs)
        max_val = max(throughputs)
        stdev = statistics.stdev(throughputs) if len(throughputs) > 1 else 0.0
        
        print(f"Average   = {avg:.2f}")
        print(f"Minimum   = {min_val:.2f}")
        print(f"Maximum   = {max_val:.2f}")
        print(f"Std Dev   = {stdev:.2f}")
        print(f"\nThe complete command logs are available in the file: {log_file}")
    else:
        print("No valid data extracted. Unable to calculate statistics.")

def main():
    print("=== Bandwidth Testing Tool (iperf) ===")
    role = input("Do you want to run the script as 'client' or 'server'? ").strip().lower()
    
    if role == "server":
        run_server()
    elif role == "client":
        run_client()
    else:
        print("Invalid choice. Restart the script and type 'client' or 'server'.")

if __name__ == "__main__":
    main()
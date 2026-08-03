"""
Project: Cyber Security incident tracker
BootCamp Day: 09
Date: 16-07-2026 
Author: 
"""
def line():
  print("========================================================================")


def header():
    line()
    print("         !!! CYBER SECURITY INCIDENT TRACKER !!!")
    line()


def menu():
    print()
    print("===============!!! MENU !!!===============")
    print(" 1. Report Incident")
    print(" 2. Assign Analyst")
    print(" 3. Change Severity")
    print(" 4. Change Status")
    print(" 5. Search Incident")
    print(" 6. Incidents status list ")
    print(" 7. Incident Statistics ")
    print(" 8. View All Incident")
    print(" 0. Exit")
    line()
    choice=int(input("Enter Your Choice : "))
    return choice



def print_list(incdnt, information):
    print(
        f"{incdnt:<8} ||"
        f" {information['severity']:<12} ||"
        f" {information['status']:<12} ||"
        f" {information['analyst']:<15} ||"
        f" {information['reported_by']:<12} ||"
        f" {information['type']}")



def print_inc(inc_id, inc):
   print("----------------------------------------")
   print(f"Incident Id   : {inc_id}")
   print(f"severity      : {inc['severity']}")
   print(f"status        : {inc['status']}")
   print(f"analyst       : {inc['analyst']}")
   print(f"reported_by   : {inc['reported_by']}")
   print(f"type          : {inc['type']}")
   print("----------------------------------------")



def print_status(count,o_count,p_count,r_count,c_count):
    print(f"========== INCIDENT STATISTICS ==========")
    print(f"Total Incidents      : {count}")
    print(f"Open                 : {o_count}")
    print(f"In Progress          : {p_count}")
    print(f"Resolved             : {r_count}")
    print(f"Closed               : {c_count}")
    print(f"========================================= ")   


def print_severity(low_count,medium_count,high_count,critical_count):
    print(f"========== SEVERITY STATISTICS ==========")
    print(f"Critical             : {critical_count}")
    print(f"High                 : {high_count}")
    print(f"Medium               : {medium_count}")
    print(f"Low                  : {low_count}")
    print(f"=========================================")

incidents = {

    "INC001": {
        "severity": "Medium",
        "status": "Open",
        "analyst": "Security Team",
        "reported_by": "Rahul",
        "type": "Phishing"
    },

    "INC002": {
        "severity": "High",
        "status": "In Progress",
        "analyst": "Amit",
        "reported_by": "Neha",
        "type": "Ransomware"
    },

    "INC003": {
        "severity": "Low",
        "status": "Resolved",
        "analyst": "Priya",
        "reported_by": "Karan",
        "type": "Malware"
    },

    "INC004": {
        "severity": "Critical",
        "status": "Open",
        "analyst": "Security Team",
        "reported_by": "Anjali",
        "type": "DDoS"
    },

    "INC005": {
        "severity": "High",
        "status": "Closed",
        "analyst": "Vikram",
        "reported_by": "Sneha",
        "type": "Unauthorized Access"
    },

    "INC006": {
        "severity": "Medium",
        "status": "In Progress",
        "analyst": "Rohit",
        "reported_by": "Pooja",
        "type": "Website Defacement"
    },

    "INC007": {
        "severity": "Critical",
        "status": "Open",
        "analyst": "Security Team",
        "reported_by": "Aditya",
        "type": "Data Leak"
    },

    "INC008": {
        "severity": "Low",
        "status": "Resolved",
        "analyst": "Meera",
        "reported_by": "Nitin",
        "type": "Spyware"
    },

    "INC009": {
        "severity": "High",
        "status": "In Progress",
        "analyst": "Sakshi",
        "reported_by": "Deepak",
        "type": "Trojan"
    },

    "INC010": {
        "severity": "Medium",
        "status": "Closed",
        "analyst": "Arjun",
        "reported_by": "Kavita",
        "type": "Brute Force Attack"
    }

}

def report_incident():
    new_id=f"INC{len(incidents)
                 +1:03d}"
    severity=input("Enter incident severity : ")
    status= input("Enter incident status : ")
    analyst=input("Enter incident analyst : ")
    reported_by=input("Enter your name : ")
    type=input("Enter incident type : ")
    
    incidents[new_id]={
        "severity": severity,
        "status": status,
        "analyst": analyst,
        "reported_by": reported_by,
        "type":  type
    }




def assign_analyst():
    inc_id="INC"+input("Enter incident id(e.g. 001) : ")
    if inc_id in incidents:
        incidents[inc_id]["analyst"]=input("Enter analyst name : ")
        print("Analyst assigned successfully.")
    else:
        print("Incident does not exit ")




def change_severity():
    inc_id="INC"+input("Enter incident id(e.g. 001) : ") 
    if inc_id in incidents:
        print(f"current severity : { incidents[inc_id]['severity']}")
        change=input("Enter severity : ").strip().lower()
        if change in("low", "medium","high", "critical"):
            incidents[inc_id]["severity"]=change.title()
        else:
            print("Invalid status!")
            return
        print(f"updated severity : { incidents[inc_id]['severity']}")

def change_status():
    inc_id="INC"+input("Enter incident id(e.g. 001) : ")
    if inc_id in incidents:
        print(f"current status : { incidents[inc_id]['status']}")
        change=input("Enter status : ").strip().lower()
        if change in("open", "in progress", "resolved", "closed"):
             incidents[inc_id]["status"]=change.title()
        else:
            print("Invalid status!")
            return
        print(f"updated status : { incidents[inc_id]['status']}")




def search_incident():
   inc_id="INC"+input("Enter incident id(e.g. 001) : ")
   if inc_id in incidents:
       inc=incidents[inc_id]
       print_inc(inc_id, inc)
    



def show_incidents(status):
    for inc_id,information in incidents.items():
        if information['status'].lower()==status:
            print_list(inc_id, information)



def incident_statistics():
    count=o_count=p_count=r_count=c_count=0
    low_count=medium_count=high_count=critical_count=0
    for incident in incidents.values():
        count+=1
        if incident['status'].lower()=="open":
            o_count+=1
        elif incident['status'].lower()=="in progress":
            p_count+=1
        elif incident['status'].lower()=="resolved":
            r_count+=1
        elif incident['status'].lower()=="closed":
            c_count+=1
        if incident['severity'].lower()=="low":
            low_count+=1
        elif incident['severity'].lower()=="medium":
            medium_count+=1
        elif incident['severity'].lower()=="high":
            high_count+=1
        elif incident['severity'].lower()=="critical":
            critical_count+=1
 
    print_status(count,o_count,p_count,r_count,c_count)
    print_severity(low_count,medium_count,high_count,critical_count)
        


def view_all_incident():
    print(f"{'ID':<8} | {'Severity':<12} | {'Status':<12} | {'Assigned To':<15} | {'Reported By':<12} | {'Type'}")
       # key     value
    for incdnt ,information in incidents.items():
        print_list(incdnt, information)



def main():
    header()
    choice=True
    while(choice):
       choice= menu()
       match choice:
          case 0:
              line()
              exit()
          case 1:
              report_incident()
          case 2:
              assign_analyst()
          case 3:
              change_severity()
          case 4:
              change_status()
          case 5:
              search_incident()
          case 6:
              status=input("Enter status ('open', 'in progress', 'resolved', 'closed') :").strip().lower()
              if status in ("open", "in progress", "resolved", "closed"):
                 show_incidents(status)
              else:
                 print("Invalid status!")
                 continue
          case 7:
              incident_statistics()
          case 8:
              view_all_incident()
          case _:
              print("!!! Invalid choice !!!")
          




main()
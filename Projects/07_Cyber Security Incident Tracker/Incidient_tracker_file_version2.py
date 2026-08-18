"""
Project: Cyber Security incident tracker(version-2)
BootCamp Day: 10
Date: 15-08-2026 
Author: yogita gothi
"""
def line():
  print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


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



def save_incidient(incidents):
  with open("incident.txt","w") as file:
   for incident in incidents:
     curnt_inc=incidents[incident]
     file.write(f"{incident}\n")
     file.write(f"severity={curnt_inc["severity"]}\n")
     file.write(f"status={curnt_inc["status"]}\n")
     file.write(f"analyst={curnt_inc["analyst"]}\n")
     file.write(f"reported_by={curnt_inc["reported_by"]}\n")
     file.write(f"type={curnt_inc["type"]}\n")
     file.write(f"\n")

   

   
def load_incident():
  incidents={}
  try:
    with open("incident.txt","r") as file: 
       while True:
          incident_id=file.readline().strip()
          if incident_id=="":
            break
          incidents[incident_id]={
            "severity":file.readline().strip().split("=")[1],
            "status":file.readline().strip().split("=")[1],
            "analyst":file.readline().strip().split("=")[1],
            "reported_by":file.readline().strip().split("=")[1],
            "type":file.readline().strip().split("=")[1],
          }
          file.readline()
  except FileNotFoundError:
     open("incident.txt","x").close()
  return incidents   


def get_next_incidident_id(incidents):
    id_list=[0]
    for incident in incidents:
        id_list.append(int(incident[3:]))
    return max(id_list)


    
def report_incident(incidents):
    new_id=f"INC{get_next_incidident_id(incidents)
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



def assign_analyst(incidents):
    inc_id="INC"+input("Enter incident id(e.g. 001) : ")
    if inc_id in incidents:
        incidents[inc_id]["analyst"]=input("Enter analyst name : ")
        print("Analyst assigned successfully.")
    else:
        print("Incident does not exit ")


def change_severity(incidents):
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


def change_status(incidents):
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


def search_incident(incidents):
   inc_id="INC"+input("Enter incident id(e.g. 001) : ")
   if inc_id in incidents:
       inc=incidents[inc_id]
       print_inc(inc_id, inc)      


def show_incidents(status, incidents):
    for inc_id,information in incidents.items():
        if information['status'].lower()==status:
            print_list(inc_id, information)



def incident_statistics(incidents):
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
        

def view_all_incident(incidents):
    print(f"{'ID':<8} | {'Severity':<12} | {'Status':<12} | {'Assigned To':<15} | {'Reported By':<12} | {'Type'}")
       # key     value
    for incdnt ,information in incidents.items():
        print_list(incdnt, information)



def main():
    header()
    incidents = load_incident()
    choice=True
    while(choice):
       choice= menu()
       match choice:
          case 0:
              line()
              exit()
          case 1:
               report_incident(incidents)
               save_incidient(incidents)
          case 2:
              assign_analyst(incidents)
              save_incidient(incidents)
          case 3:
              change_severity(incidents)
              save_incidient(incidents)
          case 4:
              change_status(incidents)
              save_incidient(incidents)
          case 5:
              search_incident(incidents)
          case 6:
              status=input("Enter status ('open', 'in progress', 'resolved', 'closed') :").strip().lower()
              if status in ("open", "in progress", "resolved", "closed"):
                 show_incidents(status, incidents)
              else:
                 print("Invalid status!")
                 continue
          case 7:
              incident_statistics(incidents)
          case 8:
              view_all_incident(incidents)
          case _:
              print("!!! Invalid choice !!!")
          


main()
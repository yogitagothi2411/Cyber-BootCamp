"""
Project: Cyber Security incident tracker(version-3)
feature-adding csv
BootCamp Day: 11
Date: 19-08-2026 
updated: 26-08-2026
Author: yogita gothi
"""
def line():
  print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


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
    try:
      choice=int(input("Enter Your Choice : "))
      return choice
    except ValueError:
        print("Invalid choice! Enter a valid number")
        return None
   



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
  with open("incident.csv","w") as file:
   for incident in incidents:
     curnt_inc=incidents[incident]
     file.write(f"{incident},{curnt_inc['severity']},{curnt_inc['status']},{curnt_inc['analyst']},{curnt_inc['reported_by']},{curnt_inc['type']}\n")
     

   

   
def load_incident():
  incidents={}
  try:
    with open("incident.csv","r") as file: 
       while True:
         line=file.readline()
         if line=="":
                break
         line=line.strip().split(",")
         if len(line)!=6:
             print("Invalid incident record: expected 6 fields")
             continue     
       # if (line[0])[3:].isdigit() and line[0][:3] =="INC":
         if line[0].startswith("INC") and (line[0])[3:].isdigit():
                incd_id=line[0]
         else:
             print("Invalid incident id")
             continue
             
             
         severity=line[1]
         if severity.lower() not in ("low", "medium", "high", "critical"):
              continue
         status=line[2]
         if status.lower() not in("open", "in progress", "resolved", "closed"):
               continue
         analyst=line[3]
         reported_by=line[4]
         type=line[5]
         if incd_id=="" or severity=="" or status=="":
             print("Invalid incident record: required field is missing")
             continue
         incidents[incd_id]={
            "severity":severity,
            "status":status,
            "analyst":analyst,
            "reported_by":reported_by,
            "type":type
        }
           
            
         
  except FileNotFoundError:
     open("incident.csv","x").close()
  return incidents   


def get_highest_incident_id(incidents):
    id_list=[0]
    for incident in incidents:
        id_list.append(int(incident[3:]))
    return max(id_list)


    
def report_incident(incidents):
    new_id=f"INC{get_highest_incident_id(incidents)
                 +1:03d}"
    severity=input("Enter incident severity : ").strip().lower()
    if severity in("low", "medium","high", "critical"):
        severity=severity.title()
    else:
        print("invalid severity")
        return
    status= input("Enter incident status : ").strip().lower()
    if status in("open", "in progress", "resolved", "closed"):
        status=status.title()
    else:
        print("invalid status")
        return
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
   else:  
       print("Id does not exist")


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
    while True:
       choice= menu()
       if choice is None:
           continue
           
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
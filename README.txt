README file
-----------

0. Please write down the full names and netids of all your team members.
    Ashleigh Chung (atc101)
    Vidya Mannava (vm479)
    
1. Briefly discuss how you implemented the LS functionality of
   tracking which TS responded to the query and timing out if neither
   TS responded.
    1) We sent the query to TS1 and then to TS2 immediately right after.
    2) LS waits for 5 seconds using .settimeout(5) 
       on the socket that connects LS to TS1 and the socket that connects LS to TS2
    3) We used nested try/except blocks (TS1's response for the outer, TS2's 
       response for the inner) to handle whether LS receives a response from the two severs.
       If TS1 responds (enters outer try block), then LS sends its response to client.
       If TS1 doesn't respond (enters outer except block), then LS checks if TS2 has responded.
    4) If TS2 has responded (enters inner try block), then LS sends its response to client.
       If TS2 has not responded (enters inner except block), then LS sends an error message to client, meaning
       that neither TS1 or TS2 have reponded.
    We sent queries to both TS1 and TS2 at the same time, however with the nested
    try/except blocks, our program is structured so that it checks for TS1's response first
    and then TS2's response if there is no TS1 response. This does not act as a problem since
    at most one of the TS servers will have the hostname in their DNS table.
        
2. Are there known issues or functions that aren't working currently in your
   attached code? If so, explain.
    - None that we know so far
    - Before running the program, manually type in 
      LS's hostname in line 46 of client.py
      TS1's hostname in line 80 of ls.py
      TS2's hostname in line 82 of ls.py
   
3. What problems did you face developing code for this project?
    The main problem we faced was determining how to make LS wait 5 seconds for 
    a response. We were also unsure about how to first check if TS1 responded 
    and only then check if TS2 responded. But once we realized we can use two 
    try/except blocks to make this work, we were able to correctly check for 
    TS1 and TS2 responses.

4. What did you learn by working on this project?
    Since this project was similar to Project 1 in terms of creating sockets, sending
    hostnames, etc., working on Project 2 only reinforced those skills for us. But what made
    Project 2 a step above Project 1 was its different structure along with the timing mechanism.
    We were able to learn how to structure the program differently (dividing Project 1's client.py 
    into Project 2's client.py and ls.py, creating ts2.py, etc.). More notably, we learned
    how to handle a situation when the server does not send any response back at all and we had to 
    rely on setting a timer to figure out its answer.
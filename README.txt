README file
-----------

In addition to your programs, you must also submit a README file with clearly
dilenated sections for the following.

0. Please write down the full names and netids of all your team members.
    Ashleigh Chung (atc101)
    Vidya Mannava (vm479)
    
1. Briefly discuss how you implemented the LS functionality of
   tracking which TS responded to the query and timing out if neither
   TS responded.
    1) We sent the query to TS1 and then to TS2 immediately right after.
    2) LS waits for 5 seconds.
    3) If TS1 responds, then LS sends its response to client.
        If TS1 doesn't respond, then LS checks if TS2 has responded.
    4) If TS2 has responded, then LS sends its response to client.
        If TS2 has not responded, then LS sends an error message to client, meaning
        that neither TS1 or TS2 have reponded.
        
2. Are there known issues or functions that aren't working currently in your
   attached code? If so, explain.
    None that we know of. 
   
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
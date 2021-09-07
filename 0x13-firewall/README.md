# 0x13. Firewall

-   By Sylvain Kalache, co-founder at Holberton School
-   Weight: 1
-   Ongoing second chance project - started 09-06-2021, must end by 09-09-2021 (in 1 day) - you're done with  0% of tasks.
-   QA review fully automated.

#### In a nutshell…

-   **Auto QA review:**  0.0/7 mandatory & 0.0/2 optional
-   **Altogether:**  **0.0%**
    -   Mandatory: 0.0%
    -   Optional: 0.0%
    -   Calculation: 0.0% + (0.0% * 0.0%) == **0.0%**

## Concepts

_For this project, students are expected to look at this concept:_

-   [Web stack debugging](https://intranet.hbtn.io/concepts/68)

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/284/V1HjQ1Y.png)

## Background Context

### Your servers without a firewall…

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/155/holbertonschool-firewall.gif)

## Resources

**Read or watch**:

-   [What is a firewall](https://intranet.hbtn.io/rltoken/QS5iHSDU_woydPRIb68sOw "What is a firewall")

## More Info

As explained in the  **web stack debugging guide**  concept page,  `telnet`  is a very good tool to check if sockets are open with  `telnet IP PORT`. For example, if you want to check if port 22 is open on  `web-02`:

```
sylvain@ubuntu$ telnet web-02.holberton.online 22
Trying 54.89.38.100...
Connected to web-02.holberton.online.
Escape character is '^]'.
SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.8

Protocol mismatch.
Connection closed by foreign host.
sylvain@ubuntu$

```

We can see for this example that the connection is successful:  `Connected to web-02.holberton.online.`

Now let’s try connecting to port 2222:

```
sylvain@ubuntu$ telnet web-02.holberton.online 2222
Trying 54.89.38.100...
^C
sylvain@ubuntu$

```

We can see that the connection never succeeds, so after some time I just use  `ctrl+c`  to kill the process.

This can be used not just for this exercise, but for any debugging situation where two pieces of software need to communicate over sockets.

Note that the school network is filtering outgoing connections (via a network-based firewall), so you might not be able to interact with certain ports on servers outside of the school network. To test your work on  `web-01`, please perform the test from outside of the school network, like from your  `web-02`  server. If you SSH into your  `web-02`  server, the traffic will be originating from  `web-02`  and not from the school’s network, bypassing the firewall.


# MSDefender-Critical-High-Monitoring
Microsoft Defender Critical &amp; High Vulnerability Monitoring with Grafana

To the contributors:

I haven't had enough time to reorganize this project's codes because I never thought I would be opening this project to someone. Some of the paragraphs are written very ugly, and there are more that can be improved. 

When you deploy this code, please check the absolute paths in the codes because you might need to modify them to match your paths. Second, please remember to check or modify your database name, table name, and column names are matched the codes.

This simple tool was developed for Advantech Corp to monitor the CVSS critical and high vulnerability counts. This tool uses Windows Task Scheduler, Python, Microsoft Defender API, Grafana, and MS SQL to complete the automatic monitoring and tracking.

![image](https://github.com/mvp314048/AUS_HighRiskMachines/assets/19400041/f434d340-ceb0-4a67-91af-8b8bd40ac876)

You will need a database to store the data, and your table structures and columns may look like the below, depending on your requirements and purposes.

![image](https://github.com/mvp314048/AUS_HighRiskMachines/assets/19400041/912709d5-c79c-429f-a953-b6b14b6fbe97)

For the visualization Server, for example, Grafana. Depending on your requirements and purposes, you can reformat and display your data like the one below.
![image](https://github.com/mvp314048/AUS_HighRiskMachines/assets/19400041/15ea84ce-49dc-460a-b01a-1ddcb0814770)

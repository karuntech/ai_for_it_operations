# Prompts for IT Operations Professionals

## Summarizing

### 1. Summarize an incident

When you need to summarize long, detailed documents such as postmortem reports, change ticket notes etc, you can use LLMs to summarize the important data.

Example post mortem report by AWS for the Oct 19&20 2025 dynamodb, NLB and EC2 issue: https://aws.amazon.com/message/101925/.

Note: You can either pass the URL to the postmortem report, or copy/paste the full postmortem report from the AWS website mentioned above.
I've found copy/pasting results in better quality response.

```text
Summarize the following incident ticket in under 300 words.  
Include: what happened, customer impact, root cause (if known), timeline, and next steps.

[PASTE INCIDENT DETAILS HERE]
```

### 2. Full RCA

When you need to create a full root cause analysis report

```text
Generate an RCA based on the incident below.  
Include sections:  
- Summary  
- Impact  
- Timeline  
- Root Cause  
- Contributing Factors  
- What Worked Well  
- What Didn’t  
- Short-term Fixes  
- Long-term Remediation  
- Action Owner Mapping

[PASTE INCIDENT DETAILS HERE]
```

### 3. Five-Why Analysis

If you are still in the same chat window,  you don't need to copy/paste the incident again. Simply enter the following prompt:

```text
Perform a 5-Whys analysis on the issue
```

### 4. Log file Anlysis

You can copy/paste an excerpt of a log file, (or even a java core dump), to summarize key findings from the log file.
Attach the log file and then enter the following prompt.

```text
Analyze the attached log file and summarize the key findings.
```

For web server access logs:

```text
Show top 10 URLs causing 500
```


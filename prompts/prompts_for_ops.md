# Prompts for IT Operations Professionals

## 1. Summarize

When you need to summarize long, detailed documents such as postmortem reports, change ticket notes etc, you can use LLMs to summarize the important data.

Example post mortem report by AWS for the Oct 19&20 2025 dynamodb, NLB and EC2 issue: https://aws.amazon.com/message/101925/.

Note: You can either pass the URL to the postmortem report, or copy/paste the full postmortem report from the AWS website mentioned above.
I've found copy/pasting results in better quality response.

```text
Summarize the following incident ticket in under 300 words.  
Include: what happened, customer impact, root cause (if known), timeline, and next steps.  
[PASTE INCIDENT HERE]
```

## 2. Full RCA

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




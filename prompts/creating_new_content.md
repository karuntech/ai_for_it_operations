# Prompts for IT Operations Professionals

## Creating new content

### 1. Email announcement

```text
I need to send an email to all users to start using 5-whys to document the root cause analysis in the problem tickets. This is important because accurate and detailed RCAs help communicate to our stakeholders correctly, enhances our knowledgebase for future troubleshooting and aid in uncovering opportunists for preventative measures. Maintain a professional tone, yet be assertive. Finish with a strong call to action. Use other examples from web as needed to make the email more compelling.
```

### 2. Playbook

```text
Take the following unstructured runbook and transform it into a structured YAML format using the template below.
Ensure that all steps fit into the corresponding sections exactly as defined—do not create new sections or reorder them.

YAML template:
title: ""
version: "1.0"
last_updated: ""
author: ""

sections:
  - overview: ""
  - prerequisites: []
  - initial_checks: []
  - failover_steps: []
  - validation: []
  - rollback: []
  - escalation: []

Unstructured runbook:
When there's an outage at our Chicago data center, we gotta move the carsbright application and all related stuff to our Boise site.  
1. check the current status if primary site is actually down  (https://carsbright.net/heathcheck)
2. Run failover script (there are a couple of scripts in the /scripts directory. Check the script names – they would have the word “dr” in them.)
3. Repoint DNS (how to do this? Ask the NS guy. The Infoblox setup keeps changing)  
4. Verify apps are running in DR . Use our Grafana dashboards. You may have to fish through to find the right dashboard (check for dashboards that start with carsbright)
5. If stuff is broken, rollback  
Escalate to someone if it’s still bad. Probably John or someone in ops.
```




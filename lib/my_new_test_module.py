#/usr/bin/env python3

ANSIBLE_METADATA = {'metatdata_version': '1.1', 'status':['preview'], 'supported_by': 'community'}

DOCUMENTATION = '''
---
module: my_new_test_module
short_description: This is my sample module
version_added: "2.4"
description: - "This is my longer description"
'''
EXAMPLE = '''
write some examples later
'''

RETURN = '''
original_message:
    description: The original name param that was passed in
    type: str
message:
    description: the outout message that the sample module generates
'''

from ansible.module_utils.basic import AnsibleModule

def run_module():
    module_args = dict(
            name=dict(type="str", required=True),
            new=dict(type="bool", required=False, default=False),
            turtle=dict(type="str", required=False, default="box"))

    result= dict(
            changed=False,
            original_message='',
            message=''
            )

    module= AnsibleModule(
            argument_spec=module_args,
            supports_check_mode=True)

    if module.check_mode:
        return result

    result["original_message"] = module.params["name"]
    result["message"] = "goodbye" + module.params["name"] + "bye forever!"

    if module.params["turtle"] != "box" :
        result["message"] = result["message"] + "Wow your" + module.params["turtle"] + "turtle is a cutie"

    if module.params["new"]:
        result["changed"]= True
    
    if module.params["name"].lower() == "hughes":
        result["message"] += "and you work at hughes, what a great place to work!! "
    
    if module.params["name"] == "fail me":
        module.fail_json(msg="You requested theh module to fail", **result)

    module.exit_json(**result)

def main():
    run_module()

if __name__=="__main__":
    main()





import sys
import os

def main():
    branch_name = os.environ['BRANCH_NAME']
    pr_num = os.environ['PR_NUM']

    print(branch_name)
    print(pr_num)
    x = branch_name.rfind('-') + 1
    env_name = branch_name[:x] + pr_num
    return env_name.upper()

if __name__ == "__main__":
    main()
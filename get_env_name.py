import sys
import os

def main():
    branch_name = os.environ['BRANCH_NAME']
    pr_num = os.environ['PR_NUM']

    print(branch_name)
    print(pr_num)
    x = branch_name.rfind('-') + 1
    print(branch_name[:x].upper() + pr_num)

if __name__ == "__main__":
    main()
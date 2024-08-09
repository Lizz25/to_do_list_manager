Feature: ToDo List Manager
    Scenario: Adding a task
        Given the To-Do list is empty
        When the user adds a task "Buy groceries"
        Then the to-do list should contain "Buy groceries"

    Scenario: List all tasks in the to-do list
        Given the to-do list contains tasks:
            | Task          |
            | Buy groceries |
            | Pay bills     |
        When the user lists all tasks
        Then the output should contain:
            """
            Tasks:
            - Buy groceries
            - Pay bills
            """

    Scenario: Mark a task as completed
        Given the to-do list contains tasks:
            | Task          | Status  |
            | Buy groceries | Pending |
        When the user marks task "Buy groceries" as completed
        Then the to-do list should show task "Buy groceries" as

    Scenario: Clear the entire to-do list
        Given the to-do list contains tasks:
            | Task          |
            | Buy groceries |
            | Pay bills     |
        When the user clears the to-do list
        Then the to-do list should be empty

    Scenario: Edit a task in the to-do list
        Given the to-do list contains tasks:
            | Task          | Status  |
            | Buy groceries | Pending |
            | Pay bills     | Pending |
        When the user edits task "Buy groceries" to "Buy household essentials" with status "Completed"
        Then the to-do list should display task "Buy household essentials" with the updated status

    Scenario: Filter tasks by status in the to-do list
        Given the to-do list contains tasks with various statuses:
            | Task                | Status    |
            | Buy groceries       | Pending   |
            | Pay bills           | Pending   |
            | Complete assignment | Completed |
        When the user filters tasks by status "Pending"
        Then the output should contain only pending tasks:
            """
            Tasks:
            - Buy groceries
            - Pay bills
            """
            
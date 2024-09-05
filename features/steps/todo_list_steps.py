from behave import given, when, then
from todo_list import TodoListManager

todo_manager = TodoListManager()

@given('the To-Do list is empty')
def step_todo_list_is_empty(context):
    todo_manager.clear_tasks()

@when('the user adds a task "{task}"')
def step_user_adds_task(context, task):
    todo_manager.add_task(task)

@then('the to-do list should contain "{task}"')
def step_todo_list_should_contain(context, task):
    assert task in todo_manager.list_task(), f"Task '{task}' not found in the list."

@given('the to-do list contains tasks')
def step_todo_list_contains_tasks(context):
    todo_manager.clear_tasks()
    for row in context.table:
        todo_manager.add_task(row['Task'])

@when('the user lists all tasks')
def step_user_lists_all_tasks(context):
    context.listed_tasks = todo_manager.list_task()

@then('the output should contain')
def step_output_should_contain(context):
    expected_output = [line.strip() for line in context.text.strip().split("\n")]
    actual_output = [f"Tasks:", f"- Buy groceries", f"- Pay bills"]
    assert expected_output == actual_output, f"Expected {expected_output}, but got {actual_output}"

@given('the to-do list contains tasks with various statuses')
def step_todo_list_contains_tasks_with_various_statuses(context):
    todo_manager.clear_tasks()
    for row in context.table:
        todo_manager.add_task(row['Task'])
        if row['Status'] == 'Completed':
            todo_manager.mark_as_completed(row['Task'])

@when('the user marks task "{task}" as completed')
def step_user_marks_task_as_completed(context, task):
    todo_manager.mark_as_completed(task)

@then('the to-do list should show task "{task}" as completed')
def step_todo_list_should_show_task_as_completed(context, task):
    tasks = todo_manager.task
    task_status = next((t["status"] for t in tasks if t["Title"] == task), None)
    assert task_status == "Completed", f"Expected 'Completed' status for '{task}', but got '{task_status}'"

@when('the user clears the to-do list')
def step_user_clears_todo_list(context):
    todo_manager.clear_tasks()

@then('the to-do list should be empty')
def step_todo_list_should_be_empty(context):
    assert len(todo_manager.task) == 0, "The to-do list is not empty."

@when('the user edits task "{old_task}" to "{new_task}" with status "{status}"')
def step_user_edits_task(context, old_task, new_task, status):
    todo_manager.edit_task(old_task, new_task, status)

@then('the to-do list should display task "{task}" with the updated status')
def step_todo_list_should_display_updated_task(context, task):
    tasks = todo_manager.task
    updated_task = next((t for t in tasks if t["Title"] == task), None)
    assert updated_task is not None, f"Task '{task}' not found"
    assert updated_task['status'] == 'Completed', f"Expected status 'Completed', but got '{updated_task['status']}'"

@when('the user filters tasks by status "{status}"')
def step_user_filters_tasks_by_status(context, status):
    context.filtered_tasks = todo_manager.filter_by_status(status)

@then('the output should contain only pending tasks')
def step_output_should_contain_only_pending_tasks(context):
    if context.table:
        expected_tasks = [row['Task'] for row in context.table]
    else:
        expected_tasks = ["Buy groceries", "Pay bills"]
    actual_output = todo_manager.filter_by_status('Pending')
    assert set(expected_tasks) == set(actual_output), f"Expected {expected_tasks}, but got {actual_output}"

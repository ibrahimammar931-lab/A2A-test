from unittest import TestCase
from app.services.tasks import create_task, get_tasks, update_task, delete_task
from app import schemas

class TestTasks(TestCase):
    def test_create_task(self):
        task = schemas.TaskCreate(title='Test Task', description='This is a test task')
        created_task = create_task(task)
        self.assertIsNotNone(created_task)
        self.assertEqual(created_task.title, task.title)
        self.assertEqual(created_task.description, task.description)

    def test_list_tasks(self):
        tasks = get_tasks()
        self.assertIsInstance(tasks, list)

    def test_update_task(self):
        task = schemas.TaskCreate(title='Test Task', description='This is a test task')
        created_task = create_task(task)
        updated_task = schemas.TaskUpdate(title='Updated Task', description='This is an updated task')
        updated = update_task(created_task.id, updated_task)
        self.assertIsNotNone(updated)
        self.assertEqual(updated.title, updated_task.title)
        self.assertEqual(updated.description, updated_task.description)

    def test_delete_task(self):
        task = schemas.TaskCreate(title='Test Task', description='This is a test task')
        created_task = create_task(task)
        deleted = delete_task(created_task.id)
        self.assertIsNotNone(deleted)
        self.assertEqual(deleted['message'], 'Deleted')
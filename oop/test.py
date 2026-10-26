# coding: utf-8

students = {
  1: {
    "name": "John",
    "age": 20,
    'gender': 'male',
    'class_num': 'A'
  },
  2: {
    "name": "Jane",
    "age": 22,
    'gender': 'female',
    'class_num': 'B'
  },
  3: {
    "name": "Tom",
    "age": 21,
    'gender': 'male',
    'class_num': 'C'
  },
  4: {
    "name": "Lucy",
    "age": 19,
    'gender': 'female',
    'class_num': 'D'
  }
  ,5: {
    "name": "Mike",
    "age": 23,
    'gender': 'male',
    'class_num': 'E'
  }
}

class NotArgError(Exception):
  def __init__(self, message):
    self.message = message
    super().__init__(self.message)

class StudentInfo(object):
  def __init__(self, students):
    self.students = students

# 检查用户信息是否合法
  def check_user_info(self, **kwargs):
    assert len(kwargs) == 4, "参数必须是4个"

    required_fields = ['name', 'age', 'gender', 'class_num']
    for field in required_fields:
      if field not in kwargs:
        return f"Missing required field: {field}"
    if not isinstance(kwargs['name'], str) or not kwargs['name']:
      return "Invalid name. It must be a non-empty string."
    if not isinstance(kwargs['age'], int) or kwargs['age'] <= 0:
      return "Invalid age. It must be a positive integer."
    if kwargs['gender'] not in ['male', 'female']:
      return "Invalid gender. It must be either 'male' or 'female'."
    if not isinstance(kwargs['class_num'], str) or not kwargs['class_num']:
      return "Invalid class number. It must be a non-empty string."
    return True

# 获取所有学生信息
  def get_all(self):
    for student_id, student_info in self.students.items():
      print(f"ID: {student_id}, Name: {student_info['name']}, Age: {student_info['age']}, Gender: {student_info['gender']}, Class: {student_info['class_num']}")
    return self.students

# 根据学生信息添加学生
  def add(self, **kwargs):
    check = self.check_user_info(**kwargs)
    if check != True:
      print(check)
      return
    self.__add(**kwargs)

# 根据学生ID删除学生信息
  def delete(self, student_id):
    if student_id in self.students:
      del self.students[student_id]
    else:
      print(f"Student with ID {student_id} does not exist.")

# 批量删除学生信息
  def deletes(self, student_ids):
    for student_id in student_ids:
      if student_id not in self.students:
        print(f"Student with ID {student_id} does not exist.")
      else:
        self.students.pop(student_id)
        print(f"Student with ID {student_id} has been deleted.")
# 根据学生ID更新学生信息
  def update(self, student_id, **kwargs):
    if student_id in self.students:
      check = self.check_user_info(**kwargs)
      if check != True:
        print(check)
        return
      self.students[student_id].update(kwargs)
    else:
      print(f"Student with ID {student_id} does not exist.")

# 批量更新学生信息
  def updates(self, students):
    for stu in students:
      try:
        id_ = list(stu.keys())[0]
        if id_ not in self.students:
          print(f"Student with ID {id_} does not exist.")
          continue
        check = self.check_user_info(**stu[id_])
        if check != True:
          print(check)
          continue
        self.students[id_] = stu[id_]
      except Exception as e:
        print(f"Error updating student with ID {id_}: {e}")

# 根据学生ID获取学生信息
  def get_by_id(self, student_id):
    if student_id in self.students:
      return self.students[student_id]
    else:
      print(f"Student with ID {student_id} does not exist.")
      return None

# 根据条件搜索学生信息
  def search(self, **kwargs):
    results = []
    for student_id, student_info in self.students.items():
      match = True
      for key, value in kwargs.items():
        if key not in student_info or student_info[key] != value:
          match = False
          break
      if match:
        results.append((student_id, student_info))
    return results
# 批量添加学生信息
  def adds(self, students_list):
    for student in students_list:
      check = self.check_user_info(**student)
      if check != True:
        print(check)
        continue
      self.__add(**student)

  def __add(self, **kwargs):
    new_id = max(self.students) + 1
    self.students[new_id] = kwargs


student_info = StudentInfo(students)
print(student_info.get_by_id(1))
student_info.add(name="Six", age=20, gender="female", class_num="F")
print(student_info.get_by_id(6))
student_info.update(6, name="Six Smith", age=21, gender="female", class_num="F")
print(student_info.get_by_id(6))
users = [
  {"name": "Seven", "age": 22, "gender": "male", "class_num": "G"},
  {"name": "Eight", "age": 23, "gender": "female", "class_num": "H" }
]
student_info.adds(users)
student_info.get_all()
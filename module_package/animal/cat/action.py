#coding: utf-8

def roar():
  return "cat roars"

def dump():
  return "cat dumps"

def run():
  return "cat runs"


class Cat:
  def __init__(self, name):
    self.name = name

  def roar(self):
    return f"{self.name} roars"

  def dump(self):
    return f"{self.name} dumps"

  def run(self):
    return f"{self.name} runs"
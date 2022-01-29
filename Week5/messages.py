message = "none yet"

def danger():
  return "Danger, Will Robinson!\n"

def safe():
  return "All clear, Will Robinson!\n"

def warning():
  return "Warning, warning!\n"

message = warning() + warning() + danger() + danger() + safe()
print(message)
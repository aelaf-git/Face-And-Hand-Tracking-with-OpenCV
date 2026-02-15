import mediapipe as mp
print("dir(mp):", dir(mp))

try:
    import mediapipe.python.solutions
    print("mediapipe.python.solutions imported successfully")
except ImportError as e:
    print("Failed to import mediapipe.python.solutions:", e)

try:
    from mediapipe.tasks import python as tasks
    print("mediapipe.tasks.python imported successfully")
    print("dir(tasks.vision):", dir(tasks.vision))
except ImportError as e:
    print("Failed to import mediapipe.tasks.python:", e)

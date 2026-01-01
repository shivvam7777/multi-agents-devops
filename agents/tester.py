from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.post("/test")
def run_tests(payload: dict):
    test_file = payload.get("file", "test_sample.py")
    
    try:
        result = subprocess.run(
            ["pytest", "-q", test_file],
            capture_output=True,
            text=True
        )
        return {
            "status": "success" if result.returncode == 0 else "fail",
            "output": result.stdout,
            "errors": result.stderr
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

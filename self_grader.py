"""
self_grader.py
学生自测评分脚本（修正版）
"""

import importlib.util
import traceback
import os
import tempfile

# ==================== 测试用例定义 ====================
tests = {
    "manage_scores": [],
    "solve_maze": [
        (
            [[0, 0, 1, 0],
             [1, 0, 0, 0],
             [0, 0, 1, 0],
             [0, 1, 0, 0]],
            [(0, 0), (0, 1), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3)]
        )
    ]
}

scores = {"manage_scores": 60, "solve_maze": 40}


# ==================== 辅助函数 ====================
def prepare_score_file():
    """创建临时学生成绩文件供测试"""
    test_file = os.path.join(tempfile.gettempdir(), "scores.txt")
    with open(test_file, "w", encoding="utf-8") as f:
        f.write("Alice,90,85,95\nBob,80,70,88\nCharlie,100,90,98\n")
    return test_file


# ==================== 评分逻辑 ====================
def grade_self():
    path = "任务二//python_advanced_assessment.py"
    if not os.path.exists(path):
        print(f"❌ 未找到 {path}，请确认文件名和路径正确。")
        return

    try:
        spec = importlib.util.spec_from_file_location("student", path)
        student = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(student)
    except Exception:
        print("❌ 无法导入你的 python_advanced_assessment.py，请检查是否存在语法错误。")
        traceback.print_exc()
        return

    print("\n📘 Python 综合考核自测评分开始\n")
    total = 0
    full = sum(scores.values())

    # ---------- manage_scores ----------
    if hasattr(student, "manage_scores"):
        try:
            test_file = prepare_score_file()
            result = student.manage_scores(test_file)
            if (
                isinstance(result, dict)
                and "students" in result
                and "class_avg" in result
                and "top_student" in result
                and abs(result["class_avg"] - 88.4) < 0.5
                and result["top_student"] == "Charlie"
            ):
                score = scores["manage_scores"]
            else:
                score = 0
        except Exception:
            traceback.print_exc()
            score = 0
        total += score
        print(f"manage_scores         {score}/{scores['manage_scores']} 分")
    else:
        print("⚠️ 未定义函数: manage_scores")

    # ---------- solve_maze ----------
    if hasattr(student, "solve_maze"):
        func = getattr(student, "solve_maze")
        case = tests["solve_maze"][0]
        try:
            result = func(case[0])
            expected = case[1]
            score = scores["solve_maze"] if result == expected else 0
        except Exception:
            traceback.print_exc()
            score = 0
        total += score
        print(f"solve_maze            {score}/{scores['solve_maze']} 分")
    else:
        print("⚠️ 未定义函数: solve_maze")

    print("\n📊 总分: {}/{} ".format(total, full))
    if total == full:
        print("🎉 恭喜！全部通过！")
    elif total >= full * 0.8:
        print("👏 表现优秀！")
    elif total >= full * 0.6:
        print("🙂 基础掌握良好")
    else:
        print("💪 继续努力，加油！")


if __name__ == "__main__":
    grade_self()

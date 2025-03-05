### **📌 README File for AI-Adaptive-Fuzzer**
This README provides instructions for **setting up, running, and troubleshooting the AI-enhanced AFL++ fuzzer**. Make sure to update paths based on your environment.

---

# **AI-Adaptive-Fuzzer**
🚀 **AI-Enhanced AFL++ for Adaptive Fuzzing** 🚀  

This repository contains an **AI-driven adaptive fuzzing framework** that integrates **Reinforcement Learning (RL) with AFL++**. The goal is to **optimize test case generation**, improve **vulnerability detection**, and enhance **fuzzing efficiency**.

---

## **1️⃣ Installation & Setup**
**🔹 Prerequisites**  
Before running the fuzzer, ensure your system has:
- **Linux OS (Ubuntu, Kali, etc.)**
- **Python 3.8+**
- **AFL++ installed**
- **Required Python libraries (Stable-Baselines3, Gym, Torch, etc.)**

### **📌 Install AFL++**
```bash
sudo apt update && sudo apt install -y build-essential python3 python3-pip cmake clang llvm
git clone https://github.com/AFLplusplus/AFLplusplus.git
cd AFLplusplus
make distrib && sudo make install
```

### **📌 Install Required Python Libraries**
```bash
pip install stable-baselines3 gym numpy pandas torch
```

---

## **2️⃣ Compiling the Target Program**
To test the AI fuzzer, compile a **vulnerable program** (e.g., **Base64 replica from LAVA-M**).

```bash
afl-clang-fast -o target_binary target_source.c
chmod +x target_binary
```
**✅ Ensure the binary runs before fuzzing:**
```bash
./target_binary test_input
```

---

## **3️⃣ Running AI-Enhanced Fuzzer**
🔹 **Make sure to change the paths as needed** before running.

```bash
python ~/AFLplusplus/run_adaptive_fuzzing.py --target ./target_binary --input ~/AFLplusplus/inputs --output ~/AFLplusplus/outputs
```

**🔹 What this does:**
- Launches the **Reinforcement Learning (RL) agent** to **select optimal mutations**.
- Executes AFL++ with **AI-driven mutation selection**.
- Logs fuzzing activity in **mutation_log.txt**.

---

## **4️⃣ Running Traditional AFL++ for Comparison**
To benchmark against standard **mutation-based fuzzing**, run:

```bash
afl-fuzz -i inputs -o outputs -- ./target_binary
```

**🔹 Why?**  
- This helps **compare performance** between **traditional fuzzing and AI-enhanced fuzzing**.
- AI fuzzing should **show better code coverage & vulnerability detection**.

---

## **5️⃣ Checking Fuzzing Results**
### **📌 AI Mutation Log**
To **see AI-selected mutations & rewards**, run:
```bash
cat ~/AFLplusplus/mutation_log.txt
```

### **📌 Code Coverage Analysis**
To **measure how much of the code was explored**, run:
```bash
cat ~/AFLplusplus/outputs/fuzzer_stats | grep "bitmap_cvg"
```

### **📌 Count Unique Crashes**
To check if new **crashes** were found:
```bash
ls -lh ~/AFLplusplus/outputs/crashes | wc -l
```

---

## **6️⃣ Debugging & Common Issues**
### **🔹 Issue: "PROGRAM ABORT : Program './target_binary' not found"**
✅ **Solution:** Recompile the binary with AFL++ instrumentation:
```bash
afl-clang-fast -o target_binary target_source.c
chmod +x target_binary
```

---

## **7️⃣ Next Steps**
🔹 **Scale fuzzing execution** across more datasets (LAVA-M, Zephyr RTOS)  
🔹 **Optimize RL model** for better training & faster learning  
🔹 **Benchmark AI vs. Traditional AFL++** and finalize results  

🚀 **This AI-enhanced AFL++ fuzzer improves efficiency, automates test case selection, and finds more vulnerabilities!** 🚀  

For questions, **open an issue or contact Hafiz Muhammad Soban Khan**. 🎯

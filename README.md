# **AI-Adaptive-Fuzzer**  
### **AI-Driven Adaptive Fuzzing for Automated Vulnerability Detection**

## **Overview**
The AI-Adaptive-Fuzzer is an **AI-enhanced fuzzing framework** that integrates **Reinforcement Learning (RL) with AFL++** to **intelligently optimize mutation strategies** for software security testing. The framework continuously adapts its fuzzing approach based on **real-time execution feedback**, improving **code coverage**, **mutation efficiency**, and **vulnerability discovery** in **embedded systems and software applications**.

This project builds upon **AFL++**, extending its capabilities with **AI-driven mutation selection and execution feedback mechanisms**. The framework has been rigorously tested on **LAVA-M (synthetic vulnerability dataset) and Zephyr RTOS (real-world embedded systems)**.

---

## **Key Features**
✅ **AI-Guided Mutation Strategy:** Uses Reinforcement Learning to **prioritize high-impact test cases**  
✅ **Adaptive Fuzzing Strategies:** Dynamically **adjusts mutation techniques** based on real-time execution feedback  
✅ **Integration with AFL++:** Utilizes an **external mutator module** to interact with AFL++ without modifying its core engine  
✅ **Real-Time Execution Feedback:** Collects **runtime coverage, execution performance, and crash data**  
✅ **Scalability Across Embedded Architectures:** Designed for **firmware, real-time OS (RTOS) testing, and security validation**  

---

## **System Architecture**
The AI-Adaptive-Fuzzer consists of multiple key components:

- **AFL++ Core Engine** – Responsible for **test case execution, instrumentation, and input mutation**  
- **AI-Driven Mutation Engine** – A Reinforcement Learning (RL)-based **decision-making module** that optimizes test case selection  
- **Execution Feedback Loop** – Collects **runtime execution results, coverage data, and crash reports** to refine mutation strategies  
- **External Mutator Module** – A bridge between **AFL++ and the AI decision-making system**  
- **Target Embedded Systems** – The fuzzer is tested on **LAVA-M (synthetic vulnerabilities) and Zephyr RTOS (real-world firmware testing)**  

---

## **Setup & Installation**
### **1️⃣ Install Dependencies**
Ensure your system has the required dependencies installed before running the AI-Adaptive-Fuzzer.

#### **🔹 Install AFL++**
```bash
sudo apt update && sudo apt install -y build-essential python3 python3-pip cmake clang llvm
git clone https://github.com/AFLplusplus/AFLplusplus.git
cd AFLplusplus
make distrib && sudo make install
```

#### **🔹 Install Python Libraries**
```bash
pip install stable-baselines3 gym numpy pandas torch
```

#### **🔹 Install Additional Tools**
```bash
sudo apt install -y gdb lcov jq
```

---

### **2️⃣ Compile the Target Program**
The target program (e.g., a **Base64 vulnerability replica from LAVA-M**) must be **compiled with AFL++ instrumentation**.

```bash
afl-clang-fast -o target_binary target_source.c
chmod +x target_binary
```
**✅ Ensure the binary runs before fuzzing:**
```bash
./target_binary test_input
```

---

### **3️⃣ Configure Input & Output Directories**
- Ensure the **input directory** contains a set of **seed test cases**.
- The **output directory** will store fuzzing results and logs.

```bash
mkdir -p ~/AFLplusplus/inputs
echo "test" > ~/AFLplusplus/inputs/testcase1
chmod -R 777 ~/AFLplusplus/inputs
mkdir -p ~/AFLplusplus/outputs
```

---

### **4️⃣ Run AI-Enhanced Fuzzing**
The AI-enhanced fuzzer should be executed with the appropriate settings.

```bash
python ~/AFLplusplus/run_adaptive_fuzzing.py --target ./target_binary --input ~/AFLplusplus/inputs --output ~/AFLplusplus/outputs
```
**🔹 What this does:**
- Launches the **Reinforcement Learning (RL) agent** to **select optimal mutations**.
- Executes AFL++ with **AI-driven mutation selection**.
- Logs fuzzing activity in **mutation_log.txt**.

---

### **5️⃣ Running Traditional AFL++ for Comparison**
To benchmark against standard **mutation-based fuzzing**, run:

```bash
afl-fuzz -i inputs -o outputs -- ./target_binary
```

**🔹 Why?**  
- This helps **compare performance** between **traditional fuzzing and AI-enhanced fuzzing**.
- AI fuzzing should **show better code coverage & vulnerability detection**.

---

## **Monitoring Execution & Collecting Results**
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

## **How It Works**
The **AI-Adaptive-Fuzzer** operates in a structured, iterative process:

1️⃣ **Fuzzing Initialization:** AFL++ generates an initial set of **baseline test cases**.  
2️⃣ **Execution & Monitoring:** The test cases are run on the **target firmware/software**, and execution feedback is collected.  
3️⃣ **AI Feedback Processing:** The RL agent **analyzes execution results** and determines the most effective mutation strategy.  
4️⃣ **Mutation Application:** New test cases are generated using **AI-optimized mutation policies** and sent back to AFL++.  
5️⃣ **Continuous Learning:** The **AI model continuously refines its mutation strategy** based on fuzzing results.  

---

## **Evaluation & Results**
The **AI-Adaptive-Fuzzer** has been tested in **real-world scenarios**:

- **LAVA-M Dataset** (Structured vulnerabilities for fuzz testing)  
- **Zephyr RTOS** (Real-time operating system for embedded systems)  

The framework is evaluated based on the following performance metrics:

- **Code Coverage Analysis** – Measures the effectiveness of test cases in exploring the software under test.  
- **Vulnerability Detection Rate** – Tracks how many unique vulnerabilities are discovered.  
- **Mutation Effectiveness** – Determines how efficiently AI-driven mutations improve the fuzzing process.  

---

## **Future Work**
🔹 **Optimize AI Model Performance:** Reduce training overhead for **faster learning cycles**.  
🔹 **Expand to More Targets:** Apply to **new embedded platforms and firmware environments**.  
🔹 **Improve Scalability:** Adapt fuzzer for **distributed execution across multiple devices**.  
🔹 **Enhance Real-Time Feedback Loop:** Fine-tune AI **decision-making for faster vulnerability discovery**.  

---

## **Contributions & Support**
This project is actively maintained, and contributions are welcome! If you encounter any issues, have feature requests, or want to collaborate, feel free to **open an issue or pull request**.

For inquiries, reach out to **Hafiz Muhammad Soban Khan**.  

🚀 **AI-Adaptive-Fuzzer: Intelligent, scalable, and efficient fuzzing for next-generation security testing!** 🚀  

---

## **License**
This project is released under the **Apache-2.0 License**. You are free to **use, modify, and distribute** the software with attribution.

---

### **📌 Summary**
- **AI-Adaptive-Fuzzer** is an **advanced fuzzing framework** integrating **AI with AFL++**.
- It applies **Reinforcement Learning (RL) to mutation selection**, optimizing **code coverage & vulnerability detection**.
- Designed for **embedded systems, firmware security, and real-time OS fuzzing**.
- Tested on **LAVA-M and Zephyr RTOS** with promising **performance improvements**.
- Future work includes **expanding target environments, optimizing AI efficiency, and improving scalability**.

🚀 **Securing embedded systems with AI-driven fuzzing!** 🚀  

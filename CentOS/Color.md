
**Customizing .bashrc or .bash_profile**:
   - Open your `.bashrc` or `.bash_profile` file in a text editor:
    
     ```
     nano ~/.bashrc
     ```     
   - Add color codes to specific commands or outputs. For example:
    
     ```bash
     export PS1="\[\e[0;32m\]\u@\h \[\e[0;36m\]\w \$ \[\e[m\]"
     ```
     This sets your command prompt (`PS1`) to display in green for the user and hostname, cyan for the current directory, and reset the color after the command prompt. There are various color codes you can use, and you can combine them to create different color schemes.

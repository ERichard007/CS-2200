FROM fedora:latest

RUN dnf install -y file python3-pip python3-devel gcc cargo rustfmt diffutils ncurses gdb fish tmux ranger vim-X11 git python3-pudb
RUN pip3 install python-Levenshtein mypy black py2cfg automata-lib
# RUN useradd -m student
# USER student
# WORKDIR /home/student

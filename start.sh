#!/bin/bash

tmux new-session -d -s bingo 'npm start'
tmux split-window -h 'source venv/bin/activate && python bingo-backend/app.py'
tmux attach-session -t bingo


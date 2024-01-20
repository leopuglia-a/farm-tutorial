import axios from "axios";
import React from "react";
import TodoItem from './Todo';


function TodoView(props) {

    return (
        <div>
            <ul>
                {props.todoList.map((todo,idx) => <TodoItem todo={todo} key={idx} />)}
            </ul>
        </div>
    )
}

export default TodoView;
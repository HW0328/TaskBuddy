import '../App.css';
import { useState } from 'react';
import classNames from 'classnames';

const App = (changePage) => {
    console.log(changePage)
    const [user, change_user] = useState("guest");
    const [isLogin, changeIsLogin] = useState(false);


    return (
        <div className="Navbar">
            <div className="nav_tab">
                <span className="Navspan">Home</span>
                <span className="Navspan">Create</span>
            </div>
            <div className="user_tab">
                    {!isLogin ? (
                        <>
                            <span className="NavspanLogin" onClick={() => changePage('signup')}>Sign up</span>
                            <span className="NavspanLogin">Sign in</span>
                        </>
                    ) : ( 
                        <>
                            <span className="NavspanLogin">Sign out</span>
                            <span className="NavspanLogin">{user}</span>
                        </>
                    )}
            </div>
        </div>
    );
};

export default App;

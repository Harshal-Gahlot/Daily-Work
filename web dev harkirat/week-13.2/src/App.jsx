import { useState } from 'react';
import './App.css';
import SideNavIcon from './components/icons/sideNav';
import Sun from './components/icons/sun';

function App() {
  const [sideBarOpen, setSideBarOpen] = useState(true);

  return (
    <div className='h-screen bg-slate-100 dark:bg-blue-700 flex'>
      <NavBar sideBarOpen={sideBarOpen} setSideBarOpen={setSideBarOpen} />
      <Main />
    </div>
  );
}

function NavBar({ sideBarOpen, setSideBarOpen }) {
  const [isMobil, setIsMobil] = useState(true);
console.log('sideBarOpen', sideBarOpen)
  if (sideBarOpen)
    return <div className="h-full bg-purple-500 flex flex-col justify-between p-2 w-[85%] xs:w-[70%] sm:w-96 shrink-0 sm:relative fixed">
      <div onClick={() => setSideBarOpen(!sideBarOpen)}>
        <SideNavIcon className='w-8 h-8 cursor-pointer ' />
      </div>

      <div onClick={() => { document.querySelector("html").classList.toggle("dark"); }}>
        <Sun className='text-white h-8 w-8 cursor-pointer' />
      </div>

    </div>;
  return <div className="w-12 h-full bg-purple-500  flex flex-col justify-between p-2">
    <div onClick={() => setSideBarOpen(!sideBarOpen)}>
      <SideNavIcon className='w-8 h-8 cursor-pointer' />
    </div>

    <div onClick={() => { document.querySelector("html").classList.toggle("dark"); }}>
      <Sun className='text-white h-8 w-8 cursor-pointer' />
    </div>
  </div>;
}

function Main() {
  return <div className='w-full'>
    <div className='bg-black h-0 md:h-32 w-full'>
    </div>
    <div className='m-4 grid grid-cols-12' >
      <div className='m-4 rounded-md shadow-xl md:block hidden col-span-3 bg-green-300 h-64 -translate-y-16'></div>
      <div className='m-4 rounded-md shadow-xl md:col-span-5 col-span-12 bg-pink-300 h-64'></div>
      <div className='m-4 rounded-md shadow-xl md:col-span-4 col-span-12 bg-orange-300 h-64'></div>
    </div>
  </div>;
}


export default App;;
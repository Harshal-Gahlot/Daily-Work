import './App.css';
import SidebarClass1 from './components/answer/1-basic-project';
import { Sidebar } from './components/Sidebar';
import { Sidebar2Transition } from './components/sidebars/Sidebar2Transition';
import { Sidebar4 } from './components/sidebars/Sidebar4';

function App() {
  // console.log("first")
  return (
    <div className='h-screen bg-blue-700'>
      {/* <SidebarClass1 /> */}

      {/* <Sidebar2Transition /> */}
      {/* <Sidebar4 /> */}
      <Sidebar />
    </div>
  );
}

export default App


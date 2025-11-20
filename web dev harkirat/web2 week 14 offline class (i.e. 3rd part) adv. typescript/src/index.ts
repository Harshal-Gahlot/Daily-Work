// import {z} from 'zod'

// const userSchema = z.string();

// export type FinalUserSchema = z.infer<typeof userSchema>
// we export this when we are using mono repos to frontend to validate at frontend runtime.




// type EventType = 'click' | 'scroll' | 'mousemove';

// type ExcludeEventType = Exclude<EventType, 'scroll'>

// const handleEvent = (event: ExcludeEventType) => {
//     console.log('event', event)
// }

// handleEvent('click')
// handleEvent('scroll') // throws error




// const users = new Map<string, number>()
// users.set("res", 4)
// users.set("pec", 5)

// const user = users.get("res")
// console.log('user', user)


// Record(below) vs Map(above) are two clean ways to do Objects



// type User = {
//     age: number;
//     name: string;
// };

// // not great/clear way
// // type Users = {
// //     [id: string]: User;
// // };

// // better/clear way to do:
// type Users = Record<string, User>

// const users: Users = {
//     "123": {age: 12, name: "123"},
//     "321": {age: 13, name: "abc"}
// }

// console.log('users', users)

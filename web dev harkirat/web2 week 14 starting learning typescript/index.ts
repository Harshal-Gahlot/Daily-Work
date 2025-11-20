interface User {
    name: string;
    age: number;
}

const x = {
    name: "a",
    age: 6,
    isTrue: true,
};

const y:User = x;

// const x: User = {
//     name: "a",
//     age: 4,
//     isTrue: true,
// };

function areLegal(users: User[]) {
    const usersCopy: User[] = [...users];
    let count: number = 0;
    for (let i = 0; i < users.length; i++) {
        if (users[i]!.age < 18) {
            usersCopy!.splice(i - count, 1)!;
            count++;
        }
    }
    return usersCopy;
}

const arr: User[] = [
    {
        name: "harshal",
        age: 69,
    },
    {
        name: "harshal2",
        age: 690,
    },
    {
        name: "harshal3",
        age: 6,
    },
    {
        name: "harshal4",
        age: 9,
    },
];

const first: User[] = areLegal(arr);

console.log(first);

// function getMax(nums: number[]): number {
//     if (nums.length === 0) {
//         return 0;
//     }
//     let maxValue = nums[0]!;

//     for (let i = 0; i < nums.length; i++) {
//         if (nums[i]! > maxValue) {
//             maxValue = nums[i]!;
//         }
//     }
//     return maxValue;
// }

// interface Admin {
//     name :string;
//     permissions: string;
// }

// // interface User {
// //     name: string;
// //     age: number;
// // }

// // const a:User = {
// //     name: 'abc',
// // }

// type UserOrAdmin = User | Admin;

// function greet (user: UserOrAdmin) {
//     console.log("hello", user.name)
// }

// interface User {
//     age: number | string
// }

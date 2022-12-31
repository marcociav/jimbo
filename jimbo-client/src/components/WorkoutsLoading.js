import React from 'react';


function WorkoutsLoading(Component) {
    return ( ({ isLoading, ...props}) => {
        if (!isLoading) return (<Component {...props}/>)
        return (
            <p style={{ fontSize: '24px' }}>
                Please wait for your workouts to load
            </p>
        )
    }

    )
}

export default WorkoutsLoading;